# $Id$
# Authority: dag

%define _bindir /bin

Summary: Berkeley VI Editor
Name: nvi
Version: 1.79
Release: 1%{?dist}
License: BSD
Group: Applications/Editors
URL: http://www.bostic.com/vi/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.sleepycat.com/pub/nvi-%{version}.tar.gz
Patch0: build.patch
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Nvi is an implementation of the ex/vi text editor originally distributed
as part of the Fourth Berkeley Software Distribution (4BSD), by
the University of California, Berkeley.

%prep
%setup
%patch0 -p0

%build
cd build/
%configure \
    --program-prefix="n" \
    --disable-curses
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -dp -m0755 %{buildroot}
%{__make} install -C build DESTDIR="%{buildroot}"

%post
if [ -x /usr/sbin/alternatives ]; then
    /usr/sbin/alternatives --install /etc/alternatives/ex ex %{_bindir}/nex 20 --slave /etc/alternatives/nex.1.gz ex.1.gz %{_mandir}/man1/nex.1.gz
    /usr/sbin/alternatives --install /etc/alternatives/vi vi %{_bindir}/nvi 20 --slave /etc/alternatives/vi.1.gz vi.1.gz %{_mandir}/man1/nvi.1.gz
    /usr/sbin/alternatives --install /etc/alternatives/view view %{_bindir}/nview 20 --slave /etc/alternatives/view.1.gz view.1.gz %{_mandir}/man1/nview.1.gz
fi

%postun
if [ -x /usr/sbin/alternatives ]; then
    /usr/sbin/alternatives --remove vi %{_bindir}/nex
    /usr/sbin/alternatives --remove vi %{_bindir}/nvi
    /usr/sbin/alternatives --remove view %{_bindir}/nview
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc FAQ LAYOUT LICENSE README docs/changelog docs/features docs/TODO docs/tutorial/
%doc %{_mandir}/man1/nex.1*
%doc %{_mandir}/man1/nvi.1*
%doc %{_mandir}/man1/nview.1*
%{_bindir}/nex
%{_bindir}/nvi
%{_bindir}/nview
%{_datadir}/vi/

%changelog
* Thu Jan 10 2008 Mikel Ward <mward@aconex.com> - 1.97-1
- Install binaries in /bin instead of /usr/bin
- Add /etc/alternatives links
- Don't install cat pages
