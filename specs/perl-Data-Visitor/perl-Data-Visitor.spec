# $Id$
# Authority: dag
# Upstream: יובל קוג'מן (Yuval Kogman) <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Visitor

Summary: Visitor style traversal of Perl data structures
Name: perl-Data-Visitor
Version: 0.26
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Visitor/

Source: http://www.cpan.org/modules/by-module/Data/Data-Visitor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Moose) >= 0.89
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::MockObject) >= 1.04
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(Tie::ToObject) >= 0.01
BuildRequires: perl(namespace::clean) >= 0.08


%description
Visitor style traversal of Perl data structures.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml SIGNATURE
%doc %{_mandir}/man3/Data::Visitor.3pm*
%doc %{_mandir}/man3/Data::Visitor::Callback.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/Visitor/
%{perl_vendorlib}/Data/Visitor.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.26-1
- Updated to version 0.26.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.25-1
- Updated to version 0.25.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.21-1
- Updated to release 0.21.

* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
