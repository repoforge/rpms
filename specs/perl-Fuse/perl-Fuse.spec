# $Id$
# Authority: dag
# Upstream: Dobrica Pavlinusic <dpavlin$rot13,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Fuse

Summary: Write filesystems in Perl using FUSE
Name: perl-Fuse
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Fuse/

Source: http://www.cpan.org/authors/id/D/DP/DPAVLIN/Fuse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, fuse-devel

%description
Write filesystems in Perl using FUSE.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Fuse.3pm*
%{perl_vendorarch}/auto/Fuse/
%{perl_vendorarch}/Fuse.pm

%changelog
* Tue Aug 19 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
