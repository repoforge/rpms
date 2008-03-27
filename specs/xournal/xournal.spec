# $Id$
# Authority: dag

Summary: Stylus oriented notetaking
Name: xournal
Version: 0.4.2
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://xournal.sourceforge.net/

Source: http://dl.sf.net/xournal/xournal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeprintui22-devel, glib2-devel >= 2.6, freetype-devel
BuildRequires: autoconf, automake

%description
Xournal is an application for notetaking, sketching, keeping a journal using 
a stylus. It is free software (GNU GPL) and runs on Linux (recent 
distributions) and other GTK+/Gnome platforms. It is similar to Microsoft 
Windows Journal or to other alternatives such as Jarnal, Gournal, and NoteLab.

%prep
%setup
./autogen.sh --prefix="%{_prefix}"
#configure

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README 
%{_bindir}/xournal
%{_datadir}/xournal/

%changelog
* Wed Mar 26 2008 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Wed Sep 09 2007 R P Herrold <info@owlriver.com> - 0.4.0.1-1
- Initial packaging.
