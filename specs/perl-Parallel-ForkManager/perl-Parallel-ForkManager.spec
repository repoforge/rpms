# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parallel-ForkManager

Summary: Simple parallel processing fork manager
Name: perl-Parallel-ForkManager
Version: 0.7.5
Release: 2.2%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parallel-ForkManager/

Source: http://www.cpan.org/modules/by-module/Parallel/Parallel-ForkManager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Share Perl variables between processes.

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
%doc Changes MANIFEST TODO
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Parallel/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.5-2.2
- Rebuild for Fedora Core 5.

* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 0.7.5-2
- Cosmetic cleanup.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.7.5-1
- Initial package. (using DAR)
