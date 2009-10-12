# $Id$
# Authority: shuff
# Upstream: Gustavo J A M Carneiro <gustavo$users,sourceforge,net>

## ExcludeDist el3 el4

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define nautilus_extensiondir %(pkg-config --variable=extensiondir libnautilus-extension)

Summary: Python bindings for Nautilus
Name: nautilus-python
Version: 0.5.0
Release: 1
License: GPL
Group: Development/Libraries
URL: http://git.gnome.org/cgit/nautilus-python

Source: http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/0.5/nautilus-python-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: eel2-devel >= 2.6
BuildRequires: gnome-python2 >= 2.12
BuildRequires: /usr/bin/libtool
BuildRequires: nautilus-devel >= 2.6
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: pygtk2-devel >= 2.8
BuildRequires: python-devel >= 2.3
BuildRequires: rpm-macros-rpmforge

Requires: /bin/cat
Requires: /sbin/ldconfig
Requires: nautilus

Provides: nautilus-python = %{version}

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

# we don't want to either provide or require anything from _docdir, per policy
%filter_provides_in %{_docdir}
%filter_requires_in %{_docdir}

# actually set up the filtering
%filter_setup

%description
These are unstable bindings for the nautilus extension library introduced in
Gnome 2.6.

%description devel
Install this package if you want to develop software using %{name}.

%prep
%setup

%build
%configure --disable-dependency-tracking
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%{__mv} %{buildroot}%{_defaultdocdir}/nautilus-python compiled_docs

%{__rm} -f %{buildroot}%{_libdir}/nautilus-python/*.la
%{__rm} -f %{buildroot}%{nautilus_extensiondir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post
/usr/bin/libtool --finish %{nautilus_extensiondir}
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README 
%dir %{nautilus_extensiondir}
%{nautilus_extensiondir}/*.so
%{_libdir}/nautilus-python/*.so

%files devel
%doc compiled_docs/examples/ compiled_docs/documentation.py
%dir %{_libdir}/pkgconfig/
%{_libdir}/pkgconfig/*

%changelog
* Fri Oct 09 2009 Steve Huff <shuff@vecna.org> - 0.5.0-1
- Initial package.

