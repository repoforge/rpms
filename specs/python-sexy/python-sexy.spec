# $Id$
# Authority:    hadams

%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define real_name sexy-python
Name:           python-sexy
Version:        0.1.9
Release:        3

Summary:        Python bindings to libsexy

Group:          System Environment/Libraries
License:        LGPL
URL:            http://www.chipx86.com/wiki/Libsexy
Source0:        http://releases.chipx86.com/libsexy/sexy-python/sexy-python-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libsexy-devel >= 0.1.10
BuildRequires:  python-devel >= 2
BuildRequires:  pygtk2-devel >= 2.8.0
BuildRequires:  libxml2-devel
Requires:  	libsexy >= 0.1.10

%description
sexy-python is a set of Python bindings around libsexy.


%prep
%setup -q -n  %{real_name}-%{version}

%build
%configure --enable-docs
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{python_sitearch}/gtk-2.0/sexy.so
%{_datadir}/pygtk/2.0/defs/sexy.defs



%changelog
* Sun Jul 22 2007 Heiko Adams <info@fedora-blog.de> - 1.4-2
- rebuild for rpmforge

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
