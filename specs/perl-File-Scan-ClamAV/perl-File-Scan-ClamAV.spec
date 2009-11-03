# $Id$
# Authority: dag
# Upstream: Colin Faber <cfaber$fpsn,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Scan-ClamAV

Summary: Connect to a local Clam Anti-Virus clamd service and send commands
Name: perl-File-Scan-ClamAV
Version: 1.91
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Scan-ClamAV/

Source: http://www.cpan.org/modules/by-module/File/File-Scan-ClamAV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: clamd
BuildRequires: perl

%description
Connect to a local Clam Anti-Virus clamd service and send commands.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/File::Scan::ClamAV.3pm*
%dir %{perl_vendorlib}/File/
%dir %{perl_vendorlib}/File/Scan/
#%{perl_vendorlib}/File/Scan/ClamAV/
%{perl_vendorlib}/File/Scan/ClamAV.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 1.91-1
- Updated to version 1.91.

* Thu Nov 22 2007 Dag Wieers <dag@wieers.com> - 1.8-1
- Initial package. (using DAR)
