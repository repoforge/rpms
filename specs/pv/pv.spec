# $Id$
# Authority: dag
# Upstream: Andrew Wood <andrew,wood$ivarch,com>

Summary: Monitor the progress of data through a pipe
Name: pv
Version: 1.1.0
Release: 1
License: Artistic
Group: Development/Tools
URL: http://www.ivarch.com/programs/pv.shtml

Source: http://www.ivarch.com/programs/sources/pv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext

%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data through a
pipeline.  It can be inserted into any normal pipeline between two processes
to give a visual indication of how quickly data is passing through, how long
it has taken, how near to completion it is, and an estimate of how long it
will be until completion.

%prep
%setup

### FIXME: When using %%makeinstall macro we get a double buildroot ! (Please fix upstream)
%{__perl} -pi.orig -e 's|\$\(RPM_BUILD_ROOT\)||g' autoconf/make/unreal.mk

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

#%post
#/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

#%preun
#/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc doc/COPYING doc/NEWS doc/TODO README
%doc %{_mandir}/man1/pv.1*
#%doc %{_infodir}/pv.info*
%{_bindir}/pv

%changelog
* Tue Jan 15 2008 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1.2
- Rebuild for Fedora Core 5.

* Sat Sep 03 2005 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Updated to release 0.9.2.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Sun Nov 07 2004 Dag Wieers <dag@wieers.com> - 0.8.9-1
- Updated to release 0.8.9.

* Wed Jun 30 2004 Dag Wieers <dag@wieers.com> - 0.8.6-1
- Updated to release 0.8.6.

* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 0.8.2-1
- Updated to release 0.8.2.

* Fri Feb 13 2004 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to release 0.7.0.

* Fri Jan 16 2004 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Initial package. (using DAR)
