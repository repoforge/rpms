# $Id$
# Authority: dag
# Upstream: David Boyce <dsb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClearCase-SyncTree

Summary: Synchronize a tree of files with a tree of elements
Name: perl-ClearCase-SyncTree
Version: 0.47
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClearCase-SyncTree/

Source: http://www.cpan.org/modules/by-module/ClearCase/ClearCase-SyncTree-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Synchronize a tree of files with a tree of elements.

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
%doc Changes MANIFEST README SYNCTREE.html
%doc %{_mandir}/man1/synctree.1*
%doc %{_mandir}/man3/ClearCase::SyncTree.3pm*
%{_bindir}/synctree
%dir %{perl_vendorlib}/ClearCase/
#%{perl_vendorlib}/ClearCase/SyncTree/
%{perl_vendorlib}/ClearCase/SyncTree.pm

%changelog
* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 0.47-1
- Initial package. (using DAR)
