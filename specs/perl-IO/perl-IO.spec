# $Id$
# Authority: dag
# Upstream: Graham Barr <gbarr$pobox,com>

### EL6 ships with perl-IO-Compress-Base-2.020-115.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-IO-Socket-INET6-2.51-2.fc6
%{?el5:# Tag: rfx}
### EL4 ships with perl-IO-String-1.08-1.1.el4
%{?el4:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO

Summary: Perl module to load various IO modules
Name: perl-IO
Version: 1.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO/

Source: http://www.cpan.org/modules/by-module/IO/IO-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-IO is a Perl module to load various IO modules.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/IO.3pm*
%doc %{_mandir}/man3/IO::*.3pm*
%{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/IO/
%{perl_vendorarch}/IO.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.25-1
- Updated to version 1.25.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.2301-1
- Switch to upstream version.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.23.1-1
- Initial package. (using DAR)
