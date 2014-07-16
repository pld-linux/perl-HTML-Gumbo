#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	Gumbo
%include	/usr/lib/rpm/macros.perl
Summary:	HTML::Gumbo - HTML5 parser based on gumbo C library
Name:		perl-HTML-Gumbo
Version:	0.12
Release:	0.1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7102b6dcff72434b519d9ab294934e28
URL:		http://search.cpan.org/dist/HTML-Gumbo/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Alien::LibGumbo)
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented
as a pure C99 library with no outside dependencies.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	config="optimize='%{rpmcflags}'" \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/HTML/*.pm
%dir %{perl_vendorarch}/auto/HTML/Gumbo
%{perl_vendorarch}/auto/HTML/Gumbo/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/HTML/Gumbo/*.so
%{_mandir}/man3/*