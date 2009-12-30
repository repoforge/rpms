# $Id$
# Authority: cmr
# Upstream: Paul Evans E<lt>leonerd$leonerd,org,ukE<gt>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Async

Summary: a collection of modules that implement asynchronous filehandle IO
Name: perl-IO-Async
Version: 0.27
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Async/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/IO-Async-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Async::MergePoint)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Heap) >= 0.8
BuildRequires: perl(IO::Poll)
BuildRequires: perl(Socket::GetAddrInfo) >= 0.08
BuildRequires: perl(Storable)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Refcount)
BuildRequires: perl(Time::HiRes)
Requires: perl(Async::MergePoint)
Requires: perl(Heap) >= 0.8
Requires: perl(IO::Poll)
Requires: perl(Socket::GetAddrInfo) >= 0.08
Requires: perl(Storable)
Requires: perl(Time::HiRes)

%filter_from_requires /^perl*/d
%filter_setup


%description
a collection of modules that implement asynchronous filehandle
IO.

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
%doc Changes MANIFEST META.yml examples/
%doc %{_mandir}/man3/IO::Async*.3pm*
%dir %{perl_vendorlib}/IO/
%{perl_vendorlib}/IO/Async/
%{perl_vendorlib}/IO/Async.pm

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.27-1
- Updated to version 0.27.

* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 0.26-1
- Updated to version 0.26.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.23-1
- Updated to version 0.23.

* Fri Aug  7 2009 Christoph Maser <cmr@financial.com> - 0.22-1
- Updated to version 0.22.

* Mon Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.21-2
- Fix deps

* Mon Jul 06 2009 Christoph Maser <cmr@financial.com> - 0.21-1
- Initial package. (using DAR)
