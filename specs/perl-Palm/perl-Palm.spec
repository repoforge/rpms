# $Id$
# Authority: dag
# Upstream: Andrew Arensburger <arensb$ooblick,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name p5-Palm
%define real_version 1.003_000

Summary: Perl Palm classes
Name: perl-Palm
Version: 1.3.0
Release: 2.2%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/p5-Palm/

Source: http://www.cpan.org/modules/by-module/Palm/p5-Palm-1.009.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Perl Palm classes.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc FAQ MANIFEST README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.0-2.2
- Rebuild for Fedora Core 5.

* Sat Oct 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.0-2
- Fixed the source url.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Initial package. (using DAR)
