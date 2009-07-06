# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest

Summary: Perl module that calculate message digests
Name: perl-Digest
Version: 1.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Digest is a Perl module that calculate message digests.

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
%doc %{_mandir}/man3/Digest.3pm*
%doc %{_mandir}/man3/Digest::base.3pm*
%doc %{_mandir}/man3/Digest::file.3pm*
%{perl_vendorlib}/Digest/
%{perl_vendorlib}/Digest.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.16-1
- Updated to version 1.16.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.15-1
- Initial package. (using DAR)
