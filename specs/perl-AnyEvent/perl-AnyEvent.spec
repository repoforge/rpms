# $Id$
# Authority: matthias
# Upstream: Marc Lehmann <schmorp@schmorp.de>
# ExcludeDist: el3

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AnyEvent
%define real_version 5.24

Summary: Framework for multiple event loops
Name: perl-AnyEvent
Version: 5.240
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AnyEvent/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/AnyEvent-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.1
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml recommends
#BuildRequires: perl(Async::Interrupt)
BuildRequires: perl(EV) >= 3.05
BuildRequires: perl(Guard) >= 1.02
BuildRequires: perl(JSON) >= 2.09
BuildRequires: perl(JSON::XS) >= 2.2
BuildRequires: perl(Net::SSLeay) >= 1.33
#Requires: perl(Async::Interrupt)
Requires: perl(EV) >= 3.05
Requires: perl(Guard) >= 1.02
Requires: perl(JSON) >= 2.09
Requires: perl(JSON::XS) >= 2.2
Requires: perl(Net::SSLeay) >= 1.33

%filter_from_requires /^perl(EV)*/d
%filter_setup


%description
AnyEvent provides a framework for multiple event loops.

%package EV
Summary: Perl AnyEvent implementation for perl-EV and libev
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}
Requires: perl(EV)

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

%package Glib
Summary: Perl AnyEvent implementation for perl-Glib
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description Glib
This subpackage contains the AnyEvent implementation for perl-Glib

%package IOAsync
Summary: Perl AnyEvent implementation for perl-IOAsync
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description IOAsync
This subpackage contains the AnyEvent implementation for perl-IOAsync

%package Irssi
Summary: Perl AnyEvent implementation for perl-Irssi
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description Irssi
This subpackage contains the AnyEvent implementation for perl-Irssi

%package POE
Summary: Perl AnyEvent implementation for perl-POE
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description POE
This subpackage contains the AnyEvent implementation for perl-POE.

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


%prep
%setup -n %{real_name}-%{real_version}

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
%doc %{_mandir}/man3/AE.3pm*
%doc %{_mandir}/man3/AnyEvent::*.3pm*
%dir %{perl_vendorlib}/AnyEvent/
%{perl_vendorlib}/AE.pm
%{perl_vendorlib}/AnyEvent.pm
%{perl_vendorlib}/AnyEvent/*.pm
%{perl_vendorlib}/AnyEvent/Impl/Perl.pm
%{perl_vendorlib}/AnyEvent/Intro.pod
%{perl_vendorlib}/AnyEvent/Util/idna.pl
%{perl_vendorlib}/AnyEvent/Util/uts46data.pl
%exclude %{perl_vendorlib}/AnyEvent/Impl/EV.pm
%exclude %{perl_vendorlib}/AnyEvent/Impl/Event.pm
%exclude %{perl_vendorlib}/AnyEvent/Impl/EventLib.pm
%exclude %{perl_vendorlib}/AnyEvent/Impl/Glib.pm
%exclude %{perl_vendorlib}/AnyEvent/Impl/IOAsync.pm
%exclude %{perl_vendorlib}/AnyEvent/Impl/Irssi.pm
%exclude %{perl_vendorlib}/AnyEvent/Impl/POE.pm
%exclude %{perl_vendorlib}/AnyEvent/Impl/Qt.pm
%exclude %{perl_vendorlib}/AnyEvent/Impl/Tk.pm

%files EV
%dir %{perl_vendorlib}/AnyEvent/Impl/
%{perl_vendorlib}/AnyEvent/Impl/EV.pm

%files Event
%dir %{perl_vendorlib}/AnyEvent/Impl/
%{perl_vendorlib}/AnyEvent/Impl/Event.pm

%files EventLib
%dir %{perl_vendorlib}/AnyEvent/Impl/
%{perl_vendorlib}/AnyEvent/Impl/EventLib.pm

%files Glib
%dir %{perl_vendorlib}/AnyEvent/Impl/
%{perl_vendorlib}/AnyEvent/Impl/Glib.pm

%files IOAsync
%dir %{perl_vendorlib}/AnyEvent/Impl/
%{perl_vendorlib}/AnyEvent/Impl/IOAsync.pm

%files Irssi
%dir %{perl_vendorlib}/AnyEvent/Impl/
%{perl_vendorlib}/AnyEvent/Impl/Irssi.pm

%files POE
%dir %{perl_vendorlib}/AnyEvent/Impl/
%{perl_vendorlib}/AnyEvent/Impl/POE.pm

%files Qt
%dir %{perl_vendorlib}/AnyEvent/Impl/
%{perl_vendorlib}/AnyEvent/Impl/Qt.pm

%files Tk
%dir %{perl_vendorlib}/AnyEvent/Impl/
%{perl_vendorlib}/AnyEvent/Impl/Tk.pm

%changelog
* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 5.24-1
- Updated to version 5.24.

* Mon Oct 12 2009 Christoph Maser <cmr@financial.com> - 5.201-1
- Updated to version 5.201.

* Thu Sep 24 2009 Steve Huff <shuff@vecna.org> - 5.2-2
- This needs Perl 5.8.1; too bad for el3.

* Thu Sep 17 2009 Steve Huff <shuff@vecna.org> - 5.2-1
- Updated to release 5.2.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 4.151-1
- Updated to release 4.151.

* Thu May 15 2008 Dries Verachtert <dries@ulyssis.org> - 3.41-1
- Updated to release 3.41.
- All implementations are now in separate subpackages.

* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 3.3-1
- Updated to release 3.3.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 2.54-1
- Updated to release 2.54.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 1.02-1
- Initial RPM release.

