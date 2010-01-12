# $Id$
# Authority: cmr
# Upstream: Paul Jamieson Fenwick <pjf@perltraining.com.au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-System-Simple

Summary: Run commands simply, with detailed diagnostics
Name: perl-IPC-System-Simple
Version: 1.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-System-Simple/

Source: http://search.cpan.org/CPAN/authors/id/P/PJ/PJF/IPC-System-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Config)
BuildRequires: perl(File::Basename)
BuildRequires: perl(List::Util)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.6.0
Requires: perl(Config)
Requires: perl(List::Util)
Requires: perl(Scalar::Util)
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup


%description
Run commands simply, with detailed diagnostics.

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
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/IPC::System::Simple.3pm*
%dir %{perl_vendorlib}/IPC/
%dir %{perl_vendorlib}/IPC/System/
#%{perl_vendorlib}/IPC/System/Simple/
%{perl_vendorlib}/IPC/System/Simple.pm

%changelog
* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 1.20-1
- Updated to version 1.20.

* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 1.19-1
- Updated to version 1.19.

* Wed Jul 08 2009 Christoph Maser <cmr@financial.com> - 1.18-1
- Initial package. (using DAR)
