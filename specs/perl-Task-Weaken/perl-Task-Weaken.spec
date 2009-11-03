# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Task-Weaken

Summary: Ensure that a platform has weaken support
Name: perl-Task-Weaken
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Task-Weaken/

Source: http://www.cpan.org/modules/by-module/Task/Task-Weaken-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(File::Spec) >= 0.8
BuildRequires: perl(Test::More) >= 0.42
Requires: perl >= 0:5.005

%description
Ensure that a platform has weaken support.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Task::Weaken.3pm*
%dir %{perl_vendorlib}/Task/
#%{perl_vendorlib}/Task/Weaken/
%{perl_vendorlib}/Task/Weaken.pm

%changelog
* Wed Jun 17 2009 Christoph Maser <cmr@financial.com> - 1.03-1
- Updated to version 1.03.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
