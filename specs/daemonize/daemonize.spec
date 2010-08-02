# $Id$
# Authority: dag
# Upstream: Brian Clapper <bmc$clapper,org>

Summary: Run a command as a Unix daemon
%define git_name bmc-daemonize
%define real_name %{git_name}-release
Name: daemonize
%define git_version f9d8e03
%define real_version 1.6-0-g%{git_version}
Version: 1.6.0
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.clapper.org/software/daemonize/

Source: http://download.github.com/bmc-daemonize-release-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
daemonize runs a command as a Unix daemon. As defined in W. Richard Stevens'
1990 book, Unix Network Programming (Addison-Wesley, 1990), a daemon is "a
process that executes 'in the background' (i.e., without an associated
terminal or login shell) either waiting for some event to occur, or waiting
to perform some specified task on a periodic basis." Upon startup, a typical
daemon program will:

- Close all open file descriptors (especially standard input, standard output
  and standard error)
- Change its working directory to the root filesystem, to ensure that it
  does not tie up another filesystem and prevent it from being unmounted
- Reset its umask value
- Run in the background (i.e., fork)
- Disassociate from its process group (usually a shell), to insulate itself
  from signals (such as HUP) sent to the process group
- Ignore all terminal I/O signals
- Disassociate from the control terminal (and take steps not to reacquire one)
- Handle any SIGCLD signals

Most programs that are designed to be run as daemons do that work for
themselves. However, you will occasionally run across one that does not.
When you must run a daemon program that does not properly make itself into a
true Unix daemon, you can use daemonize to force it to run as a true daemon.

%prep
%setup -n %{git_name}-%{git_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot} INSTALL="install -p"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG INSTALL LICENSE README*
%doc %{_mandir}/man1/daemonize.1*
%{_sbindir}/daemonize

%changelog
* Mon Jul 12 2010 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Initial package. (using DAR)
