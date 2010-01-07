# $Id$
# Authority: dag
# Upstream: Rafaël Garcia-Suarez <rgarciasuarez$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name base

Summary: Perl module to establish an ISA relationship with base classes at compile time
Name: perl-base
Version: 2.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/base/

Source: http://www.cpan.org/authors/id/R/RG/RGARCIA/base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-base is a Perl module to establish an ISA relationship with base
classes at compile time.

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
%doc %{_mandir}/man3/base.3pm*
%doc %{_mandir}/man3/fields.3pm*
%{perl_vendorlib}/base.pm
%{perl_vendorlib}/fields.pm

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 2.14-1
- Updated to version 2.14.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 2.12-1
- Initial package. (using DAR)
