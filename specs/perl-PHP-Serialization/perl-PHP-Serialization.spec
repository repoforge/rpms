# $Id$
# Authority: dag
# Upstream: Jesse Brown <jbrown$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PHP-Serialization

Summary: Convert PHP's serialize() output into Perl memory structure, and back.
Name: perl-PHP-Serialization
Version: 0.33
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PHP-Serialization/

Source: http://www.cpan.org/modules/by-module/PHP/PHP-Serialization-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Simple flexible means of converting the output of PHP's serialize() into
the equivalent Perl memory structure, and vice versa. 

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/PHP::Serialization.3pm*
%dir %{perl_vendorlib}/PHP/
#%{perl_vendorlib}/PHP/Serialization/
%{perl_vendorlib}/PHP/Serialization.pm

%changelog
* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 0.33-1
- Updated to version 0.33.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.32-1
- Updated to version 0.32.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.27-1
- Initial package. (using DAR)
