# $Id$
# Authority: dag
# Upstream: David Boyce <dsb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClearCase-ClearPrompt

Summary: Handle clearprompt in a portable, convenient way
Name: perl-ClearCase-ClearPrompt
Version: 1.31
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClearCase-ClearPrompt/

Source: http://www.cpan.org/modules/by-module/ClearCase/ClearCase-ClearPrompt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Handle clearprompt in a portable, convenient way.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README examples/
%doc %{_mandir}/man3/ClearCase::ClearPrompt.3pm*
%dir %{perl_vendorlib}/ClearCase/
#%{perl_vendorlib}/ClearCase/ClearPrompt/
%{perl_vendorlib}/ClearCase/ClearPrompt.pm

%changelog
* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 1.31-1
- Initial package. (using DAR)
