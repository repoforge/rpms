# $Id$
# Authority: dries
# Upstream: Gheorghe Pop <pop,gheorghe$rdslink,ro>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Identify resistors
Name: gresistor
Version: 0.0.1
Release: 1.2
License: GPL
Group: Applications/Engineering
URL: http://www.minipop.org/index.php?file=progs/gresistor/gresistor.tpl

Source: http://www.minipop.org/progs/gresistor/gresistor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel

%description
To allow for identification, resistors are usually marked with colored bands.
Often referred to as color codes, these markings are indicative of their
resistance, tolerance, and temperature coefficient. gResistror is a great
program that will help you translate resistor color codes into a readable
value. All you have to do is watch the colors on the resistor and then
enter them in the program. As you enter, you'll see that the resistor
value is changing according to the selected color.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --prefix %{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/gresistor
%{_datadir}/gresistor/
%{_datadir}/applications/gresistor.desktop
%{python_sitearch}/SimpleGladeApp.py*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.1-1.2
- Rebuild for Fedora Core 5.

* Mon Nov 07 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.1-1
- Initial package.
