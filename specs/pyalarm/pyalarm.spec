# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name pyAlarm

Summary: Alarm clock
Name: pyalarm
Version: 0.1.6
Release: 1.2%{?dist}
License: UNKNOWN
Group: Development/Libraries
URL: http://pyalarm.sourceforge.net/

Source: http://dl.sf.net/pyalarm/pyAlarm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python
Requires: python wxPython
Obsoletes: pyAlarm <= %{version}

%description
pyAlarm is a fancy alarm clock with plugins and stuff.

%prep
%setup -n %{real_name}-%{version}

%build
python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install --root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG DOCS LICENSE README
%{_bindir}/pyAlarmRun.py
%{_prefix}/lib/menu/pyAlarm
%{python_sitelib}/pyAlarm/
%{_datadir}/icons/*/pyAlarm.png
%{_datadir}/icons/pyAlarm.png
%{_datadir}/pyAlarm/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.6-1.2
- Rebuild for Fedora Core 5.

* Sun Mar 13 2005 Dag Wieers <dag@wieers.com> - 0.1.6-1
- Initial package. (using DAR)
