%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           pybluez
Version:        0.9.1
Release:        3%{?dist}
Summary:        Python API for the BlueZ bluetooth stack 

Group:          Development/Languages
License:        GPL
URL:            http://org.csail.mit.edu/pybluez
Source0:        http://org.csail.mit.edu/pybluez/release/pybluez-src-0.9.1.tar.gz    
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
                   
BuildRequires:      python-devel bluez-libs-devel
                   
%description
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create Bluetooth
applications.

%prep
%setup -q


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
doc/gendoc


%install
rm -rf $RPM_BUILD_ROOT
# This file shouldn't be executable - it's going into %doc
chmod a-x examples/bluezchat/bluezchat.py
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc doc/*.html README CHANGELOG COPYING examples
%{python_sitearch}/*

%changelog
* Fri Dec 29 2006 - Will Woods <wwoods@redhat.com> - 0.9.1-3
- Clean up spec file some more after further comments in bug #218678

* Fri Dec 15 2006 - Will Woods <wwoods@redhat.com> - 0.9.1-2
- Clean up spec file according to comments in bug #218678

* Wed Dec 6 2006 - Will Woods <wwoods@redhat.com> - 0.9.1-1
- Initial packaging attempt.
