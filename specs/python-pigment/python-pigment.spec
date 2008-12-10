# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name pigment-python

Summary: Python bindings to the Pigment Media Center Toolkit
Name: python-pigment
Version: 0.3.9
Release: 1
License: LGPL
Group: Applications/Multimedia
URL: http://elisa.fluendo.com/

Source: http://elisa.fluendo.com/static/download/pigment/pigment-python-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base-devel
BuildRequires: gtk2-devel
BuildRequires: pigment-devel >= 0.3.10
BuildRequires: pygtk2-devel
BuildRequires: python-devel
Requires: gstreamer-python
Requires: pigment >= 0.3.10
Requires: pygtk2

Obsoletes: pigment-python <= %{version}-%{release}
Provides: pigment-python = %{version}-%{release}

%description
Pigment is a toolkit for writing Media Center software.
These are the Python bindings for Pigment.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="install -p"

%{__mkdir} _rpm
%{__mv} %{buildroot}%{_datadir}/pigment-python/*/examples _rpm/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO _rpm/examples/
%{_datadir}/pigment-python/
%{python_sitearch}/_pgmgtkmodule.so
%{python_sitearch}/_pgmimagingmodule.so
%{python_sitearch}/_pgmmodule.so
%{python_sitelib}/pgm/
%exclude %{python_sitearch}/_pgmgtkmodule.la
%exclude %{python_sitearch}/_pgmimagingmodule.la
%exclude %{python_sitearch}/_pgmmodule.la

%changelog
* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 0.3.9-1
- Initial package. (based on fedora)
