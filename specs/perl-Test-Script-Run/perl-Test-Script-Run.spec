# $Id$
# Authority: shuff
# Upstream: sunnavy <sunnavy$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Script-Run

Summary: test the script with run
Name: perl-%{real_name}
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Script-Run/

Source: http://search.cpan.org/CPAN/authors/id/S/SU/SUNNAVY/Test-Script-Run-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(IPC::Run3)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
Requires: perl(IPC::Run3)
Requires: perl(Test::Exception)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module exports some subs to help test and run scripts in your dist's bin/
directory, if the script path is not absolute.

Nearly all the essential code is stolen from Prophet::Test, we think subs like
those should live below Test:: namespace, that's why we packed them and created
this module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Test/Script/
%{perl_vendorlib}/Test/Script/Run.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.05-1
- Updated to version 0.05.

* Tue Dec 22 2009 Steve Huff <shuff@vecna.org> - 0.03-1
- Initial package.
