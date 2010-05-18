# $Id$
# Authority: dag
# Upstream: David A. Golden <dagolden$cpan,org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-CaptureOutput

Summary: Capture STDOUT and STDERR from Perl code, subprocesses or XS
Name: perl-IO-CaptureOutput
Version: 1.1102
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-CaptureOutput/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/IO-CaptureOutput-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
#BuildRequires: perl(File::Spec) >= 3.27
BuildRequires: perl(File::Temp) >= 0.16
BuildRequires: perl(IO::File)
BuildRequires: perl(Symbol)
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::More)
Requires: perl(Carp)
Requires: perl(Exporter)
Requires: perl(File::Basename)
Requires: perl(File::Temp) >= 0.16
Requires: perl(Symbol)

%filter_from_requires /^perl*/d
%filter_setup


%description
Capture STDOUT and STDERR from Perl code, subprocesses or XS.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%doc Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README Todo examples/
%doc %{_mandir}/man3/IO::CaptureOutput.3pm*
%dir %{perl_vendorlib}/IO/
#%{perl_vendorlib}/IO/CaptureOutput/
%{perl_vendorlib}/IO/CaptureOutput.pm
%{perl_vendorlib}/IO/CaptureOutput.pod

%changelog
* Tue May 18 2010 Christoph Maser <cmaser@gmx.de> - 1.1102-1
- Updated to version 1.1102.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 1.1101-1
- Updated to version 1.1101.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 1.1000-1
- Updated to release 1.10.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 1.0801-1
- Updated to release 1.0801.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 1.0601-1
- Updated to release 1.0601.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Updated to release 1.06.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
