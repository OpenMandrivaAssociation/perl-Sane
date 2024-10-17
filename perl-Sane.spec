%define upstream_name Sane
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl extension for the SANE (Scanner Access Now Easy) Project
Source0:	http://search.cpan.org/CPAN/authors/id/R/RA/RATCLIFFE/%{upstream_name}-%{upstream_version}.tar.gz
Url:		https://search.cpan.org/dist/%{upstream_name}
BuildRequires:	perl-devel
BuildRequires:	sane-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)

%description
Perl bindings for the SANE (Scanner Access Now Easy) Project. This module
allows you to access SANE-compatible scanners in a Perlish and object-oriented
way, freeing you from the casting and memory management in C, yet remaining
very close in spirit to original API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorarch/*


%changelog
* Sat Jun 09 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.50.0-1
+ Revision: 803900
- Update to 0.05

* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.30.0-2
+ Revision: 768358
- mass rebuild of perl extensions against perl 5.14.2

* Wed Jun 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 384784
- new version

* Mon Mar 30 2009 Michael Scherer <misc@mandriva.org> 0.02-1mdv2009.1
+ Revision: 362223
- fix BuildRequires
- fix missing BuildRequires
- import perl-Sane


* Mon Mar 30 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

