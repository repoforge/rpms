# $Id$
# Authority: dries
# Upstream: &#23665;&#31185; &#27703;&#39770; <hio$hio,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-MultiLang

Summary: Multiple languages in Pod
Name: perl-Pod-MultiLang
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-MultiLang/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-MultiLang-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Pod::MultiLang*
%doc %{_mandir}/man1/mlpod2*
%{_bindir}/mlpod2html*
%{_bindir}/mlpod2pod*
%{perl_vendorlib}/Pod/MultiLang.*
%{perl_vendorlib}/Pod/MultiLang_*.pod
%{perl_vendorlib}/Pod/MultiLang/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
