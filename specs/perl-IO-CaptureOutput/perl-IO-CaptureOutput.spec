# $Id$
# Authority: dag
# Upstream: David A. Golden <dagolden$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-CaptureOutput

Summary: Capture STDOUT and STDERR from Perl code, subprocesses or XS
Name: perl-IO-CaptureOutput
Version: 1.0601
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-CaptureOutput/

Source: http://www.cpan.org/modules/by-module/IO/IO-CaptureOutput-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
#BuildRequires: perl(Test::More) >= 0.62

%description
Capture STDOUT and STDERR from Perl code, subprocesses or XS.

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
%doc Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/IO::CaptureOutput.3pm*
%dir %{perl_vendorlib}/IO/
#%{perl_vendorlib}/IO/CaptureOutput/
%{perl_vendorlib}/IO/CaptureOutput.pm
%{perl_vendorlib}/IO/CaptureOutput.pod

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 1.0601-1
- Updated to release 1.0601.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Updated to release 1.06.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
