# $Id$
# Authority: dag
# Upstream: Michael Peppler <mpeppler$peppler,org>

%{?rh7:%define _with_threaded 1}
%{?el2:%define _with_threaded 1}

%{?_with_sybase:%define sybver 12.5}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Sybase

Summary: Perl module named DBD-Sybase
Name: perl-DBD-Sybase
Version: 1.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Sybase/

Source: http://search.cpan.org/CPAN/authors/id/M/ME/MEWP/DBD-Sybase-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#%{?_with_sybase:BuildArch: i386}
BuildRequires: perl
BuildRequires: perl(DBI) >= 1.50
%{!?_with_sybase:BuildRequires: freetds-devel}
%{?_with_sybase:BuildRequires: sybase-openclient >= %{sybver}}

%description
perl-DBD-Sybase is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e '
    s|SYBASE/lib\b|SYBASE/%{_lib}|g;
    s|^configPwd.+||g;
' Makefile.PL

%build
%{!?_with_sybase:export SYBASE="/usr"}
%{?_with_sybase:export SYBASE="/opt/sybase-%{sybver}" SYBASE_OCS="OCS"}

CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
    --chained="y" \
%{!?_with_threaded:--threaded_libs="n"} \
%{?_with_threaded:--threaded_libs="y"} \
    --accept_test_defaults
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES MANIFEST META.yml README README.freetds README.vms eg/
%doc %{_mandir}/man3/DBD::Sybase.3*
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/Sybase/
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/Sybase.pm
%exclude %{perl_vendorarch}/DBD/dbd-sybase.pod

%changelog
* Tue Jan 25 2011 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.09-1
- Updated to release 1.09.

* Fri Oct 05 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Added fixes for Sybase and freetds compilation. (Tom G. Christensen)
- Initial package. (using DAR)
