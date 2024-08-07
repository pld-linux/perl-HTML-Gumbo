#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	Gumbo
Summary:	HTML::Gumbo - HTML5 parser based on gumbo C library
Name:		perl-HTML-Gumbo
Version:	0.18
Release:	8
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e6dd6060e982a7408f5b4cf7bfadd45
URL:		http://search.cpan.org/dist/HTML-Gumbo/
BuildRequires:	gumbo-parser-devel
BuildRequires:	perl(Alien::Base)
BuildRequires:	perl(Alien::LibGumbo) >= 0.03
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented
as a pure C99 library with no outside dependencies.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/HTML/*.pm
%dir %{perl_vendorarch}/auto/HTML/Gumbo
%attr(755,root,root) %{perl_vendorarch}/auto/HTML/Gumbo/*.so
%{_mandir}/man3/*
