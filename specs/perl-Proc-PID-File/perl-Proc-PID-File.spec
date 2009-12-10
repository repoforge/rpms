# $Id$
# Authority: dag
# Upstream: Erick Calder <ecalder$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-PID-File

Summary: Perl module to manage process id files
Name: perl-Proc-PID-File
Version: 1.27
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-PID-File/

Source: http://www.cpan.org/modules/by-module/Proc/Proc-PID-File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Proc-PID-File is a Perl module to manage process id files.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/Proc::PID::File.3pm*
%dir %{perl_vendorlib}/Proc/
%dir %{perl_vendorlib}/Proc/PID/
%{perl_vendorlib}/Proc/PID/File.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 1.27-1
- Updated to version 1.27.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.24-1
- Initial package. (using DAR)
