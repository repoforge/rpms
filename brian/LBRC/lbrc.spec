%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           LBRC
Version:        0.4 
Release:        1%{?dist}
Summary:        Linux Bluetooth Remote Control (LBRC)

Group:          Applications/System 
License:        GPL
URL:            http://lbrc.berlios.de/
Source0:        http://download.berlios.de/lbrc/%{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
BuildRequires:  python-devel
Requires:       pygobject2, pybluez
Requires:	python-json, dbus-python
Requires:	notify-python, gnome-python2-extras

%description
LBRC allows you to control you Linux Computer with a Java capable phone.
 
Linux Bluetooth Remote Control (LBRC) is a remote control program that
allows a Linux computer to be controlled by a J2ME device via Bluetooth.
It is divided into a server part that runs on the computer and reacts
to input events and a client part that runs on the J2ME device.
The J2ME client sends the device's keycodes, which are translated
to keystrokes, mouse movements, mouse clicks, or other input events
on the controlled computer.

%prep
%setup -q


%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --skip-build --root $RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/python-lbrc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc doc/* README CHANGELOG
%{_bindir}/*
/usr/lib/debug/usr/bin/uinputbridge.debug
%{_datadir}/lbrc
%{_datadir}/dbus-1/services/%{name}dbus.service
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}_gtk_gui

%changelog
* Mon May 14 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.4-1
- Initial RPM Release.

