# $Id$
# Authority: dag

### RHEL4 and RHEL4 have no recordmydesktop build
# ExcludeDist: el3 el4

%define desktop_vendor rpmforge

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name gtk-recordMyDesktop

Summary: GUI Desktop session recorder with audio and video
Name: gtk-recordmydesktop
Version: 0.3.8
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://recordmydesktop.iovar.org/

Source: http://dl.sf.net/recordmydesktop/gtk-recordmydesktop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pygtk2-devel
BuildRequires: python-devel
Requires: recordmydesktop >= %{version}

%description
Graphical frontend for the recordmydesktop desktop session recorder.

recordMyDesktop is a desktop session recorder for linux that attempts to be 
easy to use, yet also effective at it's primary task.

As such, the program is separated in two parts; a simple command line tool that
performs the basic tasks of capturing and encoding and an interface that 
exposes the program functionality in a usable way.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="%{__install} -c -p"
%find_lang %{real_name}

desktop-file-install --delete-original \
    --vendor="%{desktop_vendor}" \
    --dir %{buildroot}%{_datadir}/applications/ \
    %{buildroot}%{_datadir}/applications/gtk-recordmydesktop.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/gtk-recordMyDesktop
%{_datadir}/applications/%{desktop_vendor}-gtk-recordmydesktop.desktop
%{_datadir}/pixmaps/gtk-recordmydesktop.png
%{python_sitelib}/recordMyDesktop/

%changelog
* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Initial package. (using DAR)
