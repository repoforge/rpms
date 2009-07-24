# $Id$
# Authority: dag
# Upstream: Paul Evans <leonerd$leonerd,org,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Async-MergePoint

Summary: resynchronise diverged control flow
Name: perl-Async-MergePoint
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Async-MergePoint/

Source: http://www.cpan.org/modules/by-module/Async/Async-MergePoint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)

%description
resynchronise diverged control flow.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Async::MergePoint.3pm*
%dir %{perl_vendorlib}/Async/
#%{perl_vendorlib}/Async/MergePoint/
%{perl_vendorlib}/Async/MergePoint.pm

%changelog
* Fri Jul 24 2009 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
