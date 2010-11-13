# $Id$
# Authority: hadams

### EL6 ships with python-sexy-0.1.9-9.1.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name sexy-python

Summary: Python bindings to libsexy
Name: python-sexy
Version: 0.1.9
Release: 3%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.chipx86.com/wiki/Libsexy

Source: http://releases.chipx86.com/libsexy/sexy-python/sexy-python-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.0
BuildRequires: pygtk2-devel >= 2.8.0
BuildRequires: libsexy-devel >= 0.1.10
BuildRequires: libxml2-devel
Requires: libsexy >= 0.1.10

%description
sexy-python is a set of Python bindings around libsexy.


%prep
%setup -n %{real_name}-%{version}

%build
%configure --enable-docs
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{python_sitearch}/gtk-2.0/
%{python_sitearch}/gtk-2.0/sexy.so
%dir %{_datadir}/pygtk/
%dir %{_datadir}/pygtk/2.0/
%dir %{_datadir}/pygtk/2.0/defs/
%{_datadir}/pygtk/2.0/defs/sexy.defs
%exclude %{python_sitearch}/gtk-2.0/sexy.la

%changelog
* Sun Jul 22 2007 Heiko Adams <info@fedora-blog.de> - 0.1.9-3
- Rebuild for RPMforge.

* Thu Oct 26 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.9-2
- fixed requires that asked libsexy-devel instead of libsexy.

* Tue Oct 17 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.9-1
- updated to 0.1.9, license file issue has been fixed upstream

* Tue Sep 12 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.8-5
- rebuild for FC6

* Thu Aug 17 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.8-4
- Added quiet extraction of source tarball, some cleaning to the spec file

* Sun Aug 13 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.8-3
- fixed some rpmlint issues, add a patch to correct the license file

* Fri May 26 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.8-2
- Some cleaning to the spec file

* Mon May 22 2006 Karl <karlthered@gmail.com> - 0.1.8-1
- First Packaging
