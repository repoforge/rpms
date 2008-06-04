# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name matplotlib

Summary: Python plotting library
Name: python-matplotlib
Version: 0.91.2
Release: 1
License: Python
Group: Development/Libraries
URL: http://sourceforge.net/projects/matplotlib/

Source0: http://dl.sf.net/matplotlib/matplotlib-%{version}.tar.gz
Source1: setup.cfg
Patch0: matplotlib-gcc43.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: freetype-devel
BuildRequires: gtk2-devel
BuildRequires: libpng-devel
BuildRequires: pygtk2-devel
BuildRequires: python-dateutil
BuildRequires: python-devel
BuildRequires: python-numeric
BuildRequires: python-tz
BuildRequires: tkinter
BuildRequires: tk-devel
BuildRequires: zlib-devel
Requires: pycairo >= 1.2.0
Requires: python-dateutil
Requires: python-numeric
Requires: python-tz

%description
Matplotlib is a pure python plotting library with the goal of making
publication quality plots using a syntax familiar to matlab users. The
library uses Numeric for handling large data sets and supports a variety
of output backends

%package tk
Summary: Tk backend for python-matplotlib
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: tkinter

%description tk
Tk backend for python-matplotlib.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1
chmod -x lib/matplotlib/mpl-data/images/*.svg
%{__cp} -v %{SOURCE1} ./setup.cfg

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
chmod +x %{buildroot}%{python_sitearch}/matplotlib/dates.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc API_CHANGES CHANGELOG CXX INSTALL INTERACTIVE KNOWN_BUGS
%doc license/LICENSE* README TODO examples/
%{python_sitearch}/matplotlib/
%{python_sitearch}/pylab.py
%{python_sitearch}/pylab.pyc
%ghost %{python_sitearch}/pylab.pyo
%exclude %{python_sitearch}/matplotlib/backends/backend_tkagg.*
%exclude %{python_sitearch}/matplotlib/backends/tkagg.*
%exclude %{python_sitearch}/matplotlib/backends/_tkagg.so

%files tk
%dir %{python_sitearch}/matplotlib/
%dir %{python_sitearch}/matplotlib/backends/
%{python_sitearch}/matplotlib/backends/backend_tkagg.py*
%{python_sitearch}/matplotlib/backends/tkagg.py*
%{python_sitearch}/matplotlib/backends/_tkagg.so

%changelog
* Wed May 28 2008 Dag Wieers <dag@wieers.com> - 0.91.2-1
- Initial package. (using DAR)
