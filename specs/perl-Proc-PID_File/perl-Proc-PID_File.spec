# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-PID_File

Summary: Perl module to check whether a self process is already running
Name: perl-Proc-PID_File
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-PID_File/

Source: http://www.cpan.org/modules/by-module/Proc/Proc-PID_File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Proc-PID_File is a Perl module to check whether a self process
is already running.

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
%doc %{_mandir}/man3/Proc::PID_File.3pm*
%dir %{perl_vendorlib}/Proc/
%{perl_vendorlib}/Proc/PID_File.pm
%{perl_vendorlib}/Proc/simple.pl
%{perl_vendorlib}/Proc/test-T.pl

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
