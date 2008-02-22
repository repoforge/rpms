# $Id$
# Authority: dries
# Upstream: YAMASHINA Hio <hio@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-MultiLang

Summary: Multiple languages in Pod
Name: perl-Pod-MultiLang
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-MultiLang/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-MultiLang-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
Multiple languages in Pod.

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
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE example/
%doc %{_mandir}/man1/mlpod2html*.1*
%doc %{_mandir}/man1/mlpod2pod*.1*
%doc %{_mandir}/man3/Pod::MultiLang.3pm*
%doc %{_mandir}/man3/Pod::MultiLang_ja.3pm*
%doc %{_mandir}/man3/Pod::MultiLang::*.3pm*
%{_bindir}/mlpod2html*
%{_bindir}/mlpod2pod*
%dir %{perl_vendorlib}/Pod/
%{perl_vendorlib}/Pod/MultiLang/
%{perl_vendorlib}/Pod/MultiLang.mlpod
%{perl_vendorlib}/Pod/MultiLang.pm
%{perl_vendorlib}/Pod/MultiLang.pod
%{perl_vendorlib}/Pod/MultiLang_ja.pod

%changelog
* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
