%define upstream_name Sane
Name:		perl-%{upstream_name}
Version:	0.05
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl extension for the SANE (Scanner Access Now Easy) Project
Source0:	https://cpan.metacpan.org/authors/id/R/RA/RATCLIFFE/Sane-0.05.tar.gz
Url:		https://metacpan.org/dist/Sane
BuildRequires:	make
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
%setup -q -n Sane-0.05 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorarch/*


