# $Id$
# Authority: dag
# Upstream: Curtis "Ovid" Poe <ovid$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name aliased

Summary: Use shorter versions of class names
Name: perl-aliased
Version: 0.22
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/aliased/

Source: http://www.cpan.org/authors/id/O/OV/OVID/aliased-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Use shorter versions of class names.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/aliased.3pm*
#%{perl_vendorlib}/aliased/
%{perl_vendorlib}/aliased.pm

%changelog
* Sun Feb 17 2008 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 0.21-1
- Initial package. (using DAR)
