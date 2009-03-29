
%define realname   Sane
%define version    0.02
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl extension for the SANE (Scanner Access Now Easy) Project
Source:     http://www.cpan.org/modules/by-module//%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel perl(ExtUtils::Depends)
BuildRequires: sane-devel perl(ExtUtils::PkgConfig)
%description
The Sane module allows a Perl developer to use SANE-compatible scanners.
Find out more about SANE at the http://www.sane-project.org manpage.

Most methods set $Sane::STATUS, which is overloaded to give either an
integer as dictated by the SANE standard, or the the corresponding message,
as required.

Sane->get_version
    Returns an array with the SANE_VERSION_(MAJOR|MINOR|BUILD) versions:

%prep
%setup -q -n %{realname}-%{version} 

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


