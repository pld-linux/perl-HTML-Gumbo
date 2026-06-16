#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define		pdir	HTML
%define		pnam	Gumbo
Summary:	HTML::Gumbo - HTML5 parser based on gumbo C library
Summary(pl.UTF-8):	HTML::Gumbo - parser HTML5 oparty ma bibliotece C gumbo
Name:		perl-HTML-Gumbo
Version:	0.19
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/HTML/BPS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a70f17322bfef1709850e38d069003fc
URL:		https://metacpan.org/dist/HTML-Gumbo
BuildRequires:	gumbo-parser-devel
BuildRequires:	perl-Alien-Base
BuildRequires:	perl-Alien-LibGumbo >= 0.03
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Module-Build >= 0.42
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented
as a pure C99 library with no outside dependencies.

%description -l pl.UTF-8
Gumbo to implementacja algorytmu analizy HTML5, zaimplementowana jako
biblioteka w czystym C99 bez zewnętrznych zależności.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/HTML/Gumbo/*.bs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/HTML/Gumbo.pm
%dir %{perl_vendorarch}/auto/HTML/Gumbo
%{perl_vendorarch}/auto/HTML/Gumbo/Gumbo.so
%{_mandir}/man3/HTML::Gumbo.3pm*
