# $Id$
# Authority: matthias
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AnyEvent

Summary: Framework for multiple event loops
Name: perl-AnyEvent
Version: 3.3
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AnyEvent/

Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
#BuildRequires: perl(Coro)
BuildRequires: perl(Event)
BuildRequires: perl(Glib)
BuildRequires: perl(Tk)

%description
AnyEvent provides a framework for multiple event loops.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/AnyEvent.3pm*
%doc %{_mandir}/man3/AnyEvent::*.3pm*
%{perl_vendorlib}/AnyEvent/
%{perl_vendorlib}/AnyEvent.pm

%changelog
* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 3.3-1
- Updated to release 3.3.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 2.54-1
- Updated to release 2.54.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 1.02-1
- Initial RPM release.

