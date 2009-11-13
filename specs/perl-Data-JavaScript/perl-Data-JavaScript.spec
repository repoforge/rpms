# $Id$
# Authority: shuff
# Upstream: Jerrad Pierce <jpierce$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-JavaScript

Summary: Dump perl data structures into JavaScript code
Name: perl-%{real_name}
Version: 1.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-JavaScript/

Source: http://search.cpan.org/CPAN/authors/id/J/JP/JPIERCE/Data-JavaScript-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge
Requires: perl


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module is mainly intended for CGI programming, when a perl script
generates a page with client side JavaScript code that needs access to
structures created on the server.

It works by creating one line of JavaScript code per datum. Therefore,
structures cannot be created anonymously and need to be assigned to variables.
However, this format enables dumping large structures.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/*

%changelog
* Fri Nov 13 2009 Steve Huff <shuff@vecna.org> - 1.13-1
- Initial package.
