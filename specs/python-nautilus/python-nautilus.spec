# $Id$
# Authority: shuff
# Upstream: Gustavo J A M Carneiro <gustavo$users,sourceforge,net>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define nautilus_extensiondir %(pkg-config --variable=extensiondir libnautilus-extension)

%define real_name nautilus-python

Summary: Simple scripting language for Web browsing
Name: python-nautilus
Version: 0.5.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://git.gnome.org/cgit/nautilus-python

Source: http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/0.5/nautilus-python-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: eel2-devel >= 2.6
BuildRequires: gnome-python2 >= 2.12
BuildRequires: libtool
BuildRequires: nautilus-devel >= 2.6
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: pygtk2-devel >= 2.8
BuildRequires: python-devel >= 2.3

Requires: libtool
Requires: /bin/echo
Requires: /sbin/ldconfig

# we don't want to either provide or require anything from _docdir, per policy
%filter_provides_in %{_docdir}
%filter_requires_in %{_docdir}

# actually set up the filtering
%filter_setup

%description
These are unstable bindings for the nautilus extension library introduced in
Gnome 2.6.

%prep
%setup -n %{real_name}-%{version}

%build
%configure --disable-dependency-tracking
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%{__install} -d %{buildroot}%{_sysconfdir}/ld.so.conf.d/
/bin/echo > %{buildroot}%{_sysconfdir}/ld.so.conf.d/python-nautilus.conf <<LDSOCONF
/usr/lib/nautilus-python
LDSOCONF

%clean
%{__rm} -rf %{buildroot}

%post
/usr/bin/libtool --finish %{nautilus_extensiondir}
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README examples/
%dir %{_libdir}/pkgconfig/
%{_libdir}/pkgconfig/*
%dir %{nautilus_extensiondir}
%{nautilus_extensiondir}/*.so
%exclude %{nautilus_extensiondir}/*.la
%{_libdir}/nautilus-python/*.so
%exclude %{_libdir}/nautilus-python/*.la
%exclude %{_libdir}/debug/
%exclude %{_usrsrc}/debug/
%exclude %{_defaultdocdir}/
%dir %{_sysconfdir}/ld.so.conf.d/
%{_sysconfdir}/ld.so.conf.d/python-nautilus.conf

%changelog
* Thu Oct 08 2009 Steve Huff <shuff@vecna.org> - 0.5.1-1
- Initial package.

