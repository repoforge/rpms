# $Id$
# Authority: dag

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Tool for actively monitoring log files.
Name: swatch
Version: 3.1.1
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://swatch.sourceforge.net/

Source: http://dl.sf.net/swatch/swatch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Date::Calc), perl(Date::Format)
BuildRequires: perl(File::Tail), perl(Time::HiRes), perl(ExtUtils::MakeMaker)

%description
The Simple WATCHer is an automated monitoring tool that is capable
of alerting system administrators of anything that matches the
patterns described in the configuration file, whilst constantly
searching logfiles using perl.

%prep
%setup
%{__chmod} 0644 tools/*

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install PERL_INSTALL_ROOT="%{buildroot}"
%{__chmod} -R u+w %{buildroot}/*

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING COPYRIGHT KNOWN_BUGS README examples/ tools/
%doc %{_mandir}/man?/*
%{_bindir}/swatch
%{perl_vendorlib}/Swatch/
%{perl_vendorlib}/auto/Swatch/
%exclude %{perl_vendorarch}

%changelog
* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 3.1.1-1
- Updated to release 3.1.1.

* Sun Jul 25 2004 Dag Wieers <dag@wieers.com> - 3.1-1
- Initial package. (using DAR)
