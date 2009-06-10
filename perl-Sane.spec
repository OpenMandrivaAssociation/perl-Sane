%define upstream_name       Sane
%define upstream_version    0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl extension for the SANE (Scanner Access Now Easy) Project
Source:     http://search.cpan.org/CPAN/authors/id/R/RA/RATCLIFFE/%{upstream_name}-%{upstream_version}.tar.gz
Url:        http://search.cpan.org/dist/%{upstream_name}
BuildRequires: perl-devel
BuildRequires: sane-devel
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Perl bindings for the SANE (Scanner Access Now Easy) Project. This module
allows you to access SANE-compatible scanners in a Perlish and object-oriented
way, freeing you from the casting and memory management in C, yet remaining
very close in spirit to original API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
