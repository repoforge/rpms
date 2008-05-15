# $Id$
# Authority: matthias
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AnyEvent

Summary: Framework for multiple event loops
Name: perl-AnyEvent
Version: 3.41
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

%package Qt
Summary: Perl AnyEvent implementation for perl-Qt
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description Qt
This subpackage contains the AnyEvent implementation for perl-Qt.

%package Tk
Summary: Perl AnyEvent implementation for perl-Tk
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description Tk
This subpackage contains the AnyEvent implementation for perl-Tk.

%package EV
Summary: Perl AnyEvent implementation for perl-EV and libev
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description EV
This subpackage contains the AnyEvent implementation for perl-EV and libev.

%package Event
Summary: Perl AnyEvent implementation for perl-Event
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description Event
This subpackage contains the AnyEvent implementation for perl-Event.

%package EventLib
Summary: Perl AnyEvent implementation for perl-Event-Lib
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description EventLib
This subpackage contains the AnyEvent implementation for perl-Event-Lib.

%package POE
Summary: Perl AnyEvent implementation for perl-POE
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description POE
This subpackage contains the AnyEvent implementation for perl-POE.

%package Glib
Summary: Perl AnyEvent implementation for perl-Glib
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description Glib
This subpackage contains the AnyEvent implementation for perl-Glib


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
%dir %{perl_vendorlib}/AnyEvent/
%{perl_vendorlib}/AnyEvent/*.pm
%dir %{perl_vendorlib}/AnyEvent/Impl/
%{perl_vendorlib}/AnyEvent/Impl/Perl.pm
%{perl_vendorlib}/AnyEvent.pm

%files Qt
%{perl_vendorlib}/AnyEvent/Impl/Qt.pm

%files Tk
%{perl_vendorlib}/AnyEvent/Impl/Tk.pm

%files EV
%{perl_vendorlib}/AnyEvent/Impl/EV.pm

%files Event
%{perl_vendorlib}/AnyEvent/Impl/Event.pm

%files EventLib
%{perl_vendorlib}/AnyEvent/Impl/EventLib.pm

%files Glib
%{perl_vendorlib}/AnyEvent/Impl/Glib.pm

%files POE
%{perl_vendorlib}/AnyEvent/Impl/POE.pm

%changelog
* Thu May 15 2008 Dries Verachtert <dries@ulyssis.org> - 3.41-1
- Updated to release 3.41.
- All implementations are now in separate subpackages.

* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 3.3-1
- Updated to release 3.3.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 2.54-1
- Updated to release 2.54.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 1.02-1
- Initial RPM release.

